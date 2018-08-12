import * as React from "react";
import {
    ActivityIndicator,
    AsyncStorage,
    View,
} from "react-native";

import { colors, core  } from "App/style/index";
import { API } from "App/util/api/index";
import { BaseScreenProps } from "App/view/index";

export class AuthLoadingScreen extends React.Component<BaseScreenProps> {
    public api = new API();

    public componentDidMount() {
        AsyncStorage.multiGet(["username", "password"]).then(([usernamePair, passwordPair]) => {
            this.login(usernamePair[1], passwordPair[1]);
        }).catch(() =>
            this.props.navigation.navigate("Auth"),
        );
    }

    public render() {
        return (
            <View style={core.container}>
                <ActivityIndicator size={"large"} color={colors.black_primary} />
            </View>
        );
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
            this.props.navigation.navigate("Auth");
        });
    }
}
