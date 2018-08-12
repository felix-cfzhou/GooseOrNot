import * as React from "react";
import {
    ActivityIndicator,
    AsyncStorage,
    Button,
    View,
} from "react-native";
import {
    NavigationScreenConfig,
    NavigationScreenOptions,
    NavigationScreenProp,
} from "react-navigation";

import { InputText } from "App/input/text";
import { colors, core } from "App/style/index";
import { API } from "App/util/api/index";

export interface BaseScreenProps {
    navigation: NavigationScreenProp<{}>;
}

interface LoginScreenState {
    username: InputText;
    password: InputText;
    saving: boolean;
}

export class LoginScreen extends React.Component<BaseScreenProps, LoginScreenState> {
    public static readonly navigationOptions: NavigationScreenConfig<NavigationScreenOptions> = {
        title: "Login",
    };

    public api = new API();

    constructor(props: BaseScreenProps) {
        super(props);
        this.state = {
            username: new InputText({
                onValueChange: (saveFunc) => this.setState({ username: saveFunc(this.state.username) }),
                label: "Username",
                placeholder: "Username",
                initialState: "",
            }),
            password: new InputText({
                onValueChange: (saveFunc) => this.setState({ password: saveFunc(this.state.password) }),
                label: "Password",
                placeholder: "Password",
                initialState: "",
            }),
            saving: false,
        };
    }

    public componentDidMount() {
        this.setState({ saving: true });
        AsyncStorage.multiGet(["username", "password"]).then(([[uKey, uValue], [pKey, pValue]]) => {
            this.login(uValue, pValue);
        }).catch(() =>
            this.setState({ saving: false }),
        );
    }

    public render() {
        return (
            <View style={core.container}>
                <View style={{
                    paddingLeft: 20,
                    paddingRight: 20,
                    paddingTop: 5,
                    paddingBottom: 5,
                    flexDirection: "row",
                }}>
                    {this.state.username.render({
                        autoCapitalize: "none",
                        editable: !this.state.saving,
                        selectTextOnFocus: !this.state.saving,
                    })}
                </View>
                <View style={{
                    paddingLeft: 20,
                    paddingRight: 20,
                    paddingTop: 5,
                    paddingBottom: 5,
                    flexDirection: "row",
                }}>
                    {this.state.password.render({
                        autoCapitalize: "none",
                        secureTextEntry: true,
                        editable: !this.state.saving,
                        selectTextOnFocus: !this.state.saving,
                    })}
                </View>
                {this.state.saving ?
                    <ActivityIndicator size={"large"} color={colors.black_primary} />
                    : <Button
                        onPress={this.save}
                        title={"Login"}
                    />
                }
            </View>
        );
    }

    private save = () => {
        this.setState({ saving: true });
        const username = this.state.username.getState();
        const password = this.state.password.getState();
        this.login(username, password);
    }

    private login(username: string, password: string) {
        return this.api.instance_post(
            "/login",
            {
                type: "json",
                content: {
                    username,
                    password,
                },
            },
        ).then(() => {
            return AsyncStorage.multiSet([
                ["username", username],
                ["password", password],
            ]);
        }).then(() => {
            this.props.navigation.navigate("App");
        }).catch(() => {
            this.setState({ saving: false });
        });
    }
}
