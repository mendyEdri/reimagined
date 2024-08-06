// lock
// created by llama-3.1-8b-instant
export interface ILocalStorage {
  setItem(key: string, value: any): void;
  getItem(key: string): any;
  removeItem(key: string): void;
  clear(): void;
}

export class LocalStorage implements ILocalStorage {
  private storage: Storage;

  constructor() {
    this.storage = window.localStorage;
  }

  setItem(key: string, value: any): void {
    this.storage.setItem(key, JSON.stringify(value));
  }

  getItem(key: string): any {
    const value = this.storage.getItem(key);
    return value ? JSON.parse(value) : null;
  }

  removeItem(key: string): void {
    this.storage.removeItem(key);
  }

  clear(): void {
    this.storage.clear();
  }
}