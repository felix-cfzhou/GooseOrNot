import * as React from "react";
import { FlatList, Image, Text, View } from "react-native";
import { NavigationScreenConfig, NavigationScreenOptions } from "react-navigation";

import { ImageFile, parseImageFile } from "App/models/image";
import { core } from "App/style/index";
import { API } from "App/util/api/index";
import { BaseScreenProps } from "App/view/index";

interface UploadScreenState {
    images: ReadonlyArray<ImageFile>;
}

export class UploadScreen extends React.Component<BaseScreenProps, UploadScreenState> {
    public static readonly navigationOptions: NavigationScreenConfig<NavigationScreenOptions> = {
        title: "Upload",
    };

    private api = new API();

    constructor(props: BaseScreenProps) {
        super(props);
        this.state = {
            images: [],
        };
    }

    public componentDidMount() {
        this.getImages();
    }

    public render() {
        return (
            <View style={core.container}>
                <Text style={core.subtitle}>Upload an Image!</Text>
                <FlatList
                    data={this.state.images}
                    renderItem={(item) =>
                        <Image
                            source={{uri: item.item.url}}
                            style={{width: 150, height: 150}}
                        />
                    }
                    keyExtractor={(item) => item.id.toString()}
                />
            </View>
        );
    }

    private getImages() {
        return this.api.instance_get("/image").then(
            (values) => {
                if (Array.isArray(values)) {
                    const images = values.map((val) => parseImageFile(val));
                    this.setState({
                        images,
                    });
                }
            });
    }
}
