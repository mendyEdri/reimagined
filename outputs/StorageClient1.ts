// lock
// created by gpt-4o-mini
export interface ILocalStorage<T> {
    setItem(key: string, value: T): void;
    getItem(key: string): T | null;
    removeItem(key: string): void;
    clear(): void;
}

export class LocalStorage<T> implements ILocalStorage<T> {
    setItem(key: string, value: T): void {
        localStorage.setItem(key, JSON.stringify(value));
    }

    getItem(key: string): T | null {
        const item = localStorage.getItem(key);
        return item ? JSON.parse(item) as T : null;
    }

    removeItem(key: string): void {
        localStorage.removeItem(key);
    }

    clear(): void {
        localStorage.clear();
    }
}