/**
 * Goose Or Not
 *
 * @format
 * @flow
 */

import * as React from "react";
import { Text } from "react-native";
import { createDrawerNavigator, createStackNavigator, createSwitchNavigator } from "react-navigation";

import { HomeScreen } from "App/view/app/index";
import { LogoutScreen } from "App/view/app/logout";
import { UploadScreen } from "App/view/app/upload";
import { LoginScreen } from "App/view/auth/index";
import { AuthLoadingScreen } from "App/view/auth/loading";

const AuthStack = createStackNavigator({
  Login: {
    screen: LoginScreen,
  },
}, {
    headerMode: "none",
    initialRouteName: "Login",
  });

const Drawer = createDrawerNavigator({
  Home: {
    screen: HomeScreen,
  },
  Upload: {
    screen: UploadScreen,
  },
  Logout: {
    screen: LogoutScreen,
  },
}, {
    initialRouteName: "Home",
  },
);

const AppStack = createStackNavigator({
  Drawer,
}, {
    headerMode: "float",
    initialRouteName: "Drawer",
    navigationOptions: ({ navigation }) => ({
      headerLeft: <Text onPress={() => navigation.openDrawer()}> {"Menu"} </Text>,
    }),
  });

const RootStack = createSwitchNavigator({
  AuthLoading: AuthLoadingScreen,
  Auth: AuthStack,
  App: AppStack,
}, {
    initialRouteName: "AuthLoading",
  });

export class App extends React.Component<{}> {
  public render() {
    return <RootStack />;
  }
}
