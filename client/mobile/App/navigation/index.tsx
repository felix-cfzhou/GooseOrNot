/**
 * Goose Or Not
 *
 * @format
 * @flow
 */

import * as React from "react";
import { createStackNavigator } from "react-navigation";

import { HomeScreen, LoginScreen } from "App/view/index";
import { UploadScreen } from "App/view/upload";

const RootStack = createStackNavigator({
  Login: {
    screen: LoginScreen,
  },
  Home: {
    screen: HomeScreen,
  },
  Upload: {
    screen: UploadScreen,
  },
}, {
    initialRouteName: "Login",
  },
);

export class App extends React.Component<{}> {
  public render() {
    return <RootStack />;
  }
}
