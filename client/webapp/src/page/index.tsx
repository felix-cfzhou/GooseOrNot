import * as React from 'react';

import { InputFile } from 'src/input/file';
import { API } from 'src/util/api';

import logo from './logo.svg';

// tslint:disable-next-line:no-var-requires
require("./index.css");

export class HomeHeader extends React.Component<{}> {
  public render() {
    return <header className="App-header">
      <img src={logo} className="App-logo" alt="logo" />
      <h1 className="App-title">Welcome to React</h1>
      {this.props.children}
    </header>;
  }
}

interface HomePageState {
  upload: InputFile;
}

export class HomePage extends React.Component<{}, HomePageState> {
  private api = new API();

  constructor() {
    super({});
    this.state = {
      upload: new InputFile({
        initialState: null,
        onValueChange: (event) => {
          const files = event.target.files;
          if (files && files.length > 0) {
            this.api.instance_post(
              '/signed_upload',
              {
                type: "file",
                body: {
                  upload_file: files[0],
                },
              },
            );
          }
        },
      }),
    };
  }

  public render() {
    return (
      <div className="App">
        {this.state.upload.render({})}
      </div>
    );
  }
}
