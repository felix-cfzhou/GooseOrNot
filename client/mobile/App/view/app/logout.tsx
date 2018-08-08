import * as React from "react";
import { AsyncStorage, Button, Text, View } from "react-native";
import {
    NavigationScreenConfig,
    NavigationScreenOptions,
} from "react-navigation";

import { colors, core } from "App/style/index";
import { BaseScreenProps } from "App/view/index";

export class LogoutScreen extends React.Component<BaseScreenProps> {
    public static readonly navigationOptions: NavigationScreenConfig<NavigationScreenOptions> = {
        title: "Logout",
    };

    public render() {
        return (
            <View style={core.container}>
                <Text style={core.subtitle}>Logout?</Text>
                <Button
                    color={colors.pink_primary}
                    title={"Yes :("}
                    onPress={this.logout}
                />
            </View>
        );
    }

    private logout = () => {
        AsyncStorage.multiRemove(["username", "password"]).then(() => {
            this.props.navigation.navigate("Auth");
        });
    }
}
