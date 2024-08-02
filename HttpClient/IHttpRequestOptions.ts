export interface IHttpRequestOptions {
    headers?: Record<string, string>;
    credentials?: 'include' | 'same-origin' | 'omit';
    mode?: 'cors' | 'no-cors' | 'same-origin';
    redirect?: 'follow' | 'error' | 'manual';
}
