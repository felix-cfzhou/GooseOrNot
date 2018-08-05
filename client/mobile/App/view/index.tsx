import * as React from "react";
import { Platform, StyleSheet, Text, View } from "react-native";

const instructions = Platform.select({
    android:
      "Double tap R on your keyboard to reload\n" +
      "Shake or press menu button for dev menu",
    ios: "Press Cmd+R to reload,\n" + "Cmd+D or shake for dev menu",
  });

export class HomeScreen extends React.Component<{}> {
    public render() {
        return (
            <View style={styles.container}>
                <Text style={styles.welcome}>Welcome to Goose Or Not!</Text>
                <Text style={styles.instructions}>To get started, upload a picture!</Text>
                <Text style={styles.instructions}>{instructions}</Text>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#F5FCFF",
    },
    welcome: {
        fontSize: 20,
        textAlign: "center",
        margin: 10,
    },
    instructions: {
        textAlign: "center",
        color: "#333333",
        marginBottom: 5,
    },
});
