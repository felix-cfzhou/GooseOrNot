import * as React from 'react';
// tslint:disable-next-line:no-var-requires
require("./index.css");

import logo from './logo.svg';

export class HomeHeader extends React.Component<{}> {
  public render() {
    return <header className="App-header">
      <img src={logo} className="App-logo" alt="logo" />
      <h1 className="App-title">Welcome to React</h1>
      {this.props.children}
    </header>;
  }
}

const HomePageStyle = {
  backgroundColor: "#44014C"
}

export class HomePage extends React.Component<{}> {
  public render() {
    return (
      <div className="App" style ={HomePageStyle}>
        {/* FIXME: make upload compartment */}
        <form
          action={"/upload/photos"}
          method={"POST"}
          encType={"multipart/form-data"}
        >
          <input
            type={"file"}
            name={"photo"}
            multiple={true}
          />
          <input
            type={"submit"}
          />
        </form>
      </div>
    );
  }
}
