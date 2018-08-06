import * as React from "react";
import { ActivityIndicator, Button, Text, View } from "react-native";
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
                onValueChange: (saveFunc) => this.setState({username: saveFunc(this.state.username)}),
                label: "Username",
                placeholder: "Username",
                initialState: "",
            }),
            password: new InputText({
                onValueChange: (saveFunc) => this.setState({username: saveFunc(this.state.username)}),
                label: "Password",
                placeholder: "Password",
                initialState: "",
            }),
            saving: false,
        };
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
        this.setState({saving: true});
        this.api.instance_post(
            "/api/login",
            {
                username: this.state.username.state,
                password: this.state.password.state,
            },
        ).then(() => {
            this.props.navigation.navigate("Home");
            this.setState({saving: false});
        }).catch(() => {
            this.setState({saving: false});
        });
    }
}

export class HomeScreen extends React.Component<BaseScreenProps> {
    public static readonly navigationOptions: NavigationScreenConfig<NavigationScreenOptions> = {
        title: "Goose Or Not",
    };

    public render() {
        return (
            <View style={core.container}>
                <Text style={core.subtitle}>Welcome to Goose Or Not!</Text>
                <Text style={core.centered_text}>To get started, upload a picture!</Text>
                <Button
                    color={colors.pink_primary}
                    title={"Go to Upload"}
                    onPress={() => this.props.navigation.navigate("Upload")}
                />
            </View>
        );
    }
}
