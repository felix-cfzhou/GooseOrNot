import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Navigation } from './navigation';

// tslint:disable-next-line:no-var-requires
require("./index.css")

ReactDOM.render(
    <div>
        <Navigation />
    </div>,
    document.getElementById('root') as HTMLElement
);
