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

interface JsonBody {
    type: "json";
    content: JSONObject;
}

interface FileBody {
    type: "file";
    content: {[key: string]: File};
}

type Body = | JsonBody | FileBody;

type RequestMethod = "GET" | "POST" | "PUT" | "DELETE";

interface JSONObject {[key: string]: JSONValue | undefined; }
interface SpecificJSONArray<T extends JSONValue> extends Array<T> {}
interface JSONArray extends SpecificJSONArray<JSONObject> {}
type JSONValue = null | boolean | string | number | JSONArray | JSONObject;

export class API {
    private readonly baseUrl = Config.API_URL;

    public instance_get(path: string) {
        return this.request({path, method: "GET"});
    }

    public instance_delete(path: string) {
        return this.request({path, method: "DELETE"});
    }

    public instance_post(path: string, body: Body) {
        return this.request({path, method: "POST", body});
    }

    public instance_put(path: string, body: Body) {
        return this.request({path, method: "PUT", body});
    }

    public request(req: {
        path: string,
        method: RequestMethod,
        body?: Body,
    }): Bluebird<JSONValue> {
        const url = `${this.baseUrl}/api${req.path}`;
        let body: RequestInit["body"];
        if (req.body) {
            if (req.body.type === "json") {
                body = JSON.stringify(req.body.content);
            } else if (req.body.type === "file") {
                const formData = new FormData();
                for (const key in req.body.content) {
                    if (req.body.content.hasOwnProperty(key)) {
                        formData.append(key, req.body.content[key]);
                    }
                }
                body = formData;
            }
        }
        const params: RequestInit = {
            method: req.method,
            body,
        };
        const request = new Request(url, params);
        return Bluebird.resolve(fetch(request)).then((response) => {
            if (response.ok) {
                return Bluebird.resolve(response.json() as Bluebird<JSONValue>);
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
