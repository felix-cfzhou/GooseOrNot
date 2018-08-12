import { JSONObject, JSONValue, valueAsDict } from "App/util/json/index";

// tslint:disable-next-line:interface-over-type-literal
export type ImageFile = {
    id: number;
    file_name: string;
    url: string;
};

function isImageFile(object: JSONObject): object is ImageFile {
    return typeof object.id === "number"
    && typeof object.file_name === "string"
    && typeof object.url === "string";
}

export function parseImageFile(value: JSONValue): ImageFile {
    const dict = valueAsDict(value);
    if (isImageFile(dict)) {
        return dict;
    } else {
        throw new Error("parsed unexpected object");
    }
}
