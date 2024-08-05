export interface IFirebaseClient<T> {
    getData(id: string): Promise<T>;
    updateData(id: string, data: T): Promise<void>;
}