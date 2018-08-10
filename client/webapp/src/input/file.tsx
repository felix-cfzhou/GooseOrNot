import * as React from "react";

import { InputBase, InputBaseProps } from "src/input";

interface InputFileProps extends InputBaseProps<FileList | null> {
    onValueChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
}

export class InputFile extends InputBase<FileList | null> {
    private onValueChange: (event: React.ChangeEvent<HTMLInputElement>) => void;

    constructor(props: InputFileProps) {
        super(props);
        this.onValueChange = props.onValueChange;
    }

    public render(extraProps: React.InputHTMLAttributes<HTMLInputElement>): React.ReactNode {
        return <input
            type={"file"}
            onChange={this.onValueChange}
            value={""}
            disabled={this.props.disabled}
            {...extraProps}
        />;
    }

    public save = (saveFunc: (data: FileList | null) => void): void => {
        saveFunc(this.state);
    }
}
