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
    public api = new API({ "Content-Type": "application/json" });

    public componentDidMount() {
        AsyncStorage.multiGet(["username", "password"]).then(([[uKey, uValue], [pKey, pValue]]) => {
            this.login(uValue, pValue);
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
                username,
                password,
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
