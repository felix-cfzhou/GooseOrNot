/**
 * Goose Or Not
 *
 * @format
 * @flow
 */

import * as React from "react";
import { createStackNavigator } from "react-navigation";

import { HomeScreen } from "App/view";

const RootStack = createStackNavigator({
  Home: {
    screen: HomeScreen,
  },
});

export class App extends React.Component<{}> {
  public render() {
    return <RootStack />;
  }
}
