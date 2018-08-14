export interface JSONObject {[key: string]: JSONValue | undefined; }
export interface SpecificJSONArray<T extends JSONValue> extends Array<T> {}
export interface JSONArray extends SpecificJSONArray<JSONObject> {}
export type JSONValue = null | boolean | string | number | JSONArray | JSONObject;

const isJSONObject = function(value: JSONValue): value is JSONObject {
    return typeof value === "object" && value != null && !Array.isArray(value);
};

export const valueAsDict = (value: JSONValue) => {
    if (isJSONObject(value)) {
        return value;
    } else {
        throw new Error("value is not an Object");
    }
};
