import { StyleSheet } from "react-native";

import { colors } from "App/style/index";

export const inputStyle = StyleSheet.create({
    text: {
        height: 40,
        borderColor: colors.black_primary,
        borderWidth: 2.5,
        borderRadius: 7.5,
        textAlign: "left",
        width: "100%",
        backgroundColor: colors.white,
    },
});
