export interface IHttpClient {
    get(url: string, options?: IRequestOptions): Promise<IResponse>;
    post(url: string, body: any, options?: IRequestOptions): Promise<IResponse>;
    delete(url: string, options?: IRequestOptions): Promise<IResponse>;
}

export interface IRequestOptions {
    headers?: Record<string, string>;
    queryParams?: Record<string, string>;
}

export interface IResponse {
    status: number;
    data: any;
}