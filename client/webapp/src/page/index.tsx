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

export class HomePage extends React.Component<{}> {
  public render() {
    return (
      <div className="App">
        {/* FIXME: make upload compartment */}
        <form
          action={"/api/signed_upload"}
          method={"POST"}
          encType={"multipart/form-data"}
        >
          <input
            type={"file"}
            name={"upload_file"}
          />
          <input
            type={"submit"}
          />
        </form>
      </div>
    );
  }
}
