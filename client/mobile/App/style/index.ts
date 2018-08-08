import { StyleSheet } from "react-native";

// official waterloo color palette https://uwaterloo.ca/brand/visual-expression/colour-palette
export const colors = {
    gold1: "#FFFFAA",
    gold2: "#FFEA3D",
    gold3: "#FFD54F",
    gold4: "#E4B429",
    gold_primary: "#FFD54F",
    black1: "#DFDFDF",
    black2: "#A2A2A2",
    black3: "#787878",
    black4: "#000000",
    black_primary: "#000000",
    white: "#FFFFFF",
    pink1: "#FFBEEF",
    pink2: "#FF63AA",
    pink3: "#DF2498",
    pink4: "#C60078",
    pink_primary: "#C60068",
};

export const fontSize = {
    small: 10,
    medium: 20,
    large: 40,
    huge: 80,
};

export const core = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: colors.gold_primary,
    },
    subtitle: {
        fontSize: fontSize.medium,
        textAlign: "center",
        margin: 10,
    },
    centered_text: {
        textAlign: "center",
        color: colors.black_primary,
        marginBottom: 5,
    },
});
