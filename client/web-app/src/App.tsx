import * as React from 'react';
// tslint:disable-next-line:no-var-requires
require("./App.css")

import logo from './logo.svg';

class App extends React.Component<{}> {
  public render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        // FIXME: make upload compartment
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

export default App;
