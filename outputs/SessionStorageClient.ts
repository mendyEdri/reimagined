export interface ISessionStorage<T> {
    setItem(key: string, value: T): void;
    getItem(key: string): T | null;
    removeItem(key: string): void;
    clear(): void;
}

export class SessionStorage<T> implements ISessionStorage<T> {
    setItem(key: string, value: T): void {
        sessionStorage.setItem(key, JSON.stringify(value));
    }

    getItem(key: string): T | null {
        const item = sessionStorage.getItem(key);
        return item ? JSON.parse(item) as T : null;
    }

    removeItem(key: string): void {
        sessionStorage.removeItem(key);
    }

    clear(): void {
        sessionStorage.clear();
    }
}