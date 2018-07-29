import * as React from "react";
import * as io from "socket.io-client";

interface ExampleSocketPageState {
    history: ReadonlyArray<string>;
    inputState: string;
}

export class ExampleSocketPage extends React.Component<{}, ExampleSocketPageState> {
    private readonly NAMESPACE_TEST = '/socket/test';
    private socket: SocketIOClient.Socket;

    constructor(props: {}) {
        super(props);
        this.state = {
            history: [],
            inputState: "",
        };

        this.socket = io(this.NAMESPACE_TEST);
        this.socket.on('disconnect', () => {
            this.updateHistory(`disconnected from ${this.NAMESPACE_TEST}`);
        });
        this.socket.on('json', (json: {data: string}) => {
            this.updateHistory(json.data);
        });
        this.socket.on('message', (msg: string) => {
            this.updateHistory(msg);
        });
    }

    public render() {
        const history = this.state.history.map((entry, ind) =>
            <li key={ind}>{entry}</li>,
        );

        return (
            <div>
                <form onSubmit={this.onSubmit}>
                    <input type="text" value={this.state.inputState} onChange={this.onValueChange} />
                    <input type="submit" value="Submit" />
                </form>
                <button
                    onClick={() => {
                        if(this.state.inputState !== "") {
                            this.setState({inputState: ""});
                            this.socket.emit('json', {
                                data: this.state.inputState,
                            });
                        }
                    }}   
                >
                    {"EMIT json"}
                </button>
                <ul>
                    {history}
                </ul>
            </div>
        );
    }

    private onValueChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        this.setState({
            inputState: event.target.value,
        });
    }

    private onSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        if(this.state.inputState !== "") {
            this.setState({inputState: ""});
            this.emitMessage(this.state.inputState);
        }
    }

    private updateHistory(entry: string) {
        const newHis = Array.from(this.state.history);
        newHis.push(entry);
        this.setState({
            history: newHis,
        });
    }

    private emitMessage = (message: string) => {
        this.socket.send(message);
    }
}