import * as React from "react";
import { TextInput, TextInputProps } from "react-native";

import { InputBase, InputBaseProps } from "App/input/index";

import { inputStyle } from "./style";

interface InputTextProps extends InputBaseProps<string> {
    onValueChange: (updateFunc: (prevInput: InputText) => InputText) => void;
}

export class InputText extends InputBase<string> {
    private onValueChange: (updateFunc: (prevInput: InputText) => InputText) => void;

    constructor(props: InputTextProps) {
        super(props);
        this.onValueChange = props.onValueChange;
    }

    public render(extraProps: TextInputProps): React.ReactNode {
        return <TextInput
            style={inputStyle.text}
            onChangeText={(text: string) => {
                this.state = text;
                this.onValueChange(this.updateFunc);
            }}
            value={this.state}
            placeholder={this.props.placeholder}
            {...extraProps}
        />;
    }

    public save = (saveFunc: (data: string) => void): void => {
        saveFunc(this.state);
    }

    private updateFunc: (prevInput: InputText) => InputText = (prevInput: InputText) => {
        return new InputText({
            label: this.props.label,
            initialState: prevInput.state,
            onValueChange: this.onValueChange,
        });
    }
}
