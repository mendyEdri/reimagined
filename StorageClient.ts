export interface IStorage<T> {
    setItem(key: string, value: T): void;
    getItem(key: string): T | null;
    removeItem(key: string): void;
    clear(): void;
}

export class LocalStorage<T> implements IStorage<T> {
    setItem(key: string, value: T): void {
        localStorage.setItem(key, JSON.stringify(value));
    }

    getItem(key: string): T | null {
        const item = localStorage.getItem(key);
        return item ? JSON.parse(item) : null;
    }

    removeItem(key: string): void {
        localStorage.removeItem(key);
    }

    clear(): void {
        localStorage.clear();
    }
}