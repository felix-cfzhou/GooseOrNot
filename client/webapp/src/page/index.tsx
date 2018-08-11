import * as Bluebird from "bluebird";
import * as React from 'react';

import { InputFile } from 'src/input/file';
import { ImageFile, parseImageFile } from 'src/models/image';
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
  images: ReadonlyArray<ImageFile>;
  loading: boolean;
}

export class HomePage extends React.Component<{}, HomePageState> {
  private api = new API();

  constructor() {
    super({});
    this.state = {
      loading: false,
      upload: new InputFile({
        initialState: null,
        onValueChange: this.onFileChange,
      }),
      images: [],
    };
  }

  public componentDidMount() {
    this.getImages();
  }

  public render() {
    return (
      <div className="HomePage">
        {this.state.upload.render({})}
        {this.state.images.map((im) => <img src={im.url} key={im.id}/>)}
      </div>
    );
  }

  private onFileChange: (event: React.ChangeEvent<HTMLInputElement>) => void
  = (event) => {
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
      ).then((image) =>
        Bluebird.resolve(
          this.setState({
            images: Array.of(parseImageFile(image), ...this.state.images),
          }),
        ),
      );
    }
  }

  private getImages() {
    return this.api.instance_get('/image/query').then(
      (values: Array<ImageFile>) => {
        this.setState({
          images: values,
        });
    });
  }
}
