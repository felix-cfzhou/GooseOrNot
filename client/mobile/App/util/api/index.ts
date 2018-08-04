import Bluebird from "bluebird";
import Config from "react-native-config";

interface RequestErrorProps {
    content: string;
    status: number;
    message: string;
}

class RequestError extends Error {
    public status: number;
    public content: string;

    public constructor({content, status, message}: RequestErrorProps) {
        super(message);
        this.status = status;
        this.content = content;
    }
}

type RequestMethod = "GET" | "POST" | "PUT" | "DELETE";

interface JSONObject {[key: string]: JSONValue | undefined; }
interface SpecificJSONArray<T extends JSONValue> extends Array<T> {}
interface JSONArray extends SpecificJSONArray<JSONObject> {}
type JSONValue = null | boolean | string | number | JSONArray | JSONObject;

export class API {
    private static readonly baseUrl = Config.API_URL;
    private static readonly headers = {
        Accept: "application/json",
    };

    public instance_get(path: string) {
        return this.request({path, method: "GET"});
    }

    public instance_delete(path: string) {
        return this.request({path, method: "DELETE"});
    }

    public instance_post(path: string, body: JSONObject) {
        return this.request({path, method: "POST", body});
    }

    public instance_put(path: string, body: JSONObject) {
        return this.request({path, method: "PUT", body});
    }

    public request(req: {
        path: string,
        method: RequestMethod,
        body?: JSONObject,
    }): Bluebird<JSONValue> {
        const url = `${API.baseUrl}${req.path}`;
        const params: RequestInit = {
            headers: API.headers,
            method: req.method,
            body: req.body ? JSON.stringify(req.body) : undefined,
        };
        const request = new Request(url, params);
        return Bluebird.resolve(fetch(request)).then((response) => {
            if (response.ok) {
                if (response.status === 204) {
                    return Bluebird.resolve(null);
                } else {
                    return Bluebird.resolve(response.json() as Bluebird<JSONValue>);
                }
            } else {
                return response.json().then((data) => {
                    return Bluebird.reject(
                        new RequestError({
                            content: data ? data : {},
                            status: response.status,
                            message: `Unexpected status ${response.status}:${response.statusText}`,
                        }),
                    );
                });
            }
        });
    }

}
