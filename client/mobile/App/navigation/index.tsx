/**
 * Goose Or Not
 *
 * @format
 * @flow
 */

import * as React from "react";
import { createStackNavigator } from "react-navigation";

import { HomeScreen } from "App/view";
import { UploadScreen } from "App/view/upload";

const RootStack = createStackNavigator({
  Home: {
    screen: HomeScreen,
  },
  Upload: {
    screen: UploadScreen,
  },
}, {
    initialRouteName: "Home",
  },
);

export class App extends React.Component<{}> {
  public render() {
    return <RootStack />;
  }
}
