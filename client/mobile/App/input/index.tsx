import * as React from "react";

export interface InputBaseProps<InputType> {
    label?: string;
    placeholder?: string;
    initialState: InputType;
}

export abstract class InputBase<InputType> {
    public abstract save: (saveFunc: (data: InputType) => void) => void;
    public props: InputBaseProps<InputType>;
    public state: InputType;

    protected label: string = "";

    constructor(props: InputBaseProps<InputType>) {
        this.props = props;
        this.state = this.props.initialState;
    }

    public abstract render(extraProps: {}): React.ReactNode;
}
