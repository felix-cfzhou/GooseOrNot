import * as React from "react";
import { Text, View } from "react-native";
import { NavigationScreenConfig, NavigationScreenOptions } from "react-navigation";

import { core } from "App/style";
import { BaseScreenProps } from "App/view"

export class UploadScreen extends React.Component<BaseScreenProps> {
    public static readonly navigationOptions: NavigationScreenConfig<NavigationScreenOptions> = {
        title: "Upload",
    };

    public render() {
        return (
            <View style={core.container}>
                <Text style={core.subtitle}>Upload an Image!</Text>
            </View>
        );
    }
}
