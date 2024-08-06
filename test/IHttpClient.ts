export interface IHttpClient<T, Y> {
    get<T>(url: string): Promise<Y>
}