import * as React from "react";
import { Button, Text, View } from "react-native";
import {
    NavigationScreenConfig,
    NavigationScreenOptions,
    NavigationScreenProp,
} from "react-navigation";

import { core } from "App/style";
import { colors } from "App/style";

export interface BaseScreenProps {
    navigation: NavigationScreenProp<{}>;
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
