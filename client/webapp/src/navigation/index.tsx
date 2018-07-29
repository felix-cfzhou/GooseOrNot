import * as React from 'react';
import { BrowserRouter, Link, Redirect, Route, Switch } from 'react-router-dom';

import { HomeHeader, HomePage } from 'src/page';
import { ExampleSocketPage } from 'src/page/sockets';

export class Navigation extends React.Component<{}> {
    public render() {
        return <BrowserRouter basename={'/webapp'}>
            <div>
                <HomeHeader/>
                <nav>
                        <ul>
                            <li><Link to='/'>Home</Link></li>
                            <li><Link to='/socket'>Socket</Link></li>
                        </ul>
                    </nav>
                <Switch>
                    <Route exact path={'/'} component={HomePage} />
                    <Route path={'/socket'} component={ExampleSocketPage} />
                    <Redirect to={'/'} />
                </Switch>
            </div>
        </BrowserRouter>;
    }

}
