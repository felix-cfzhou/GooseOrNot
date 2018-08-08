import * as React from "react";

export interface InputBaseProps<InputType> {
    label?: string;
    placeholder?: string;
    initialState: InputType;
}

export abstract class InputBase<InputType> {
    public abstract readonly save: (saveFunc: (data: InputType) => void) => void;
    public readonly props: InputBaseProps<InputType>;
    protected readonly state: InputType;
    protected label: string = "";

    constructor(props: InputBaseProps<InputType>) {
        this.props = props;
        this.state = this.props.initialState;
    }

    public getState(): InputType {
        return this.state;
    }

    public abstract render(extraProps: {}): React.ReactNode;
}
