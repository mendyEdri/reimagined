export interface IFirebaseConfig {
    apiKey: string;
    authDomain: string;
    databaseURL: string;
    projectId: string;
    storageBucket: string;
    messagingSenderId: string;
    appId: string;
}

export interface IFirebaseConnection {
    initialize(config: IFirebaseConfig): void;
    getDatabase(): IDatabase;
}

export interface IDatabase {
    setData(path: string, data: any): Promise<void>;
    getData(path: string): Promise<any>;
}

export class FirebaseConnection implements IFirebaseConnection {
    private firebase: any;

    public initialize(config: IFirebaseConfig): void {
        this.firebase = require('firebase/app');
        this.firebase.initializeApp(config);
    }

    public getDatabase(): IDatabase {
        return new FirebaseDatabase(this.firebase.database());
    }
}

class FirebaseDatabase implements IDatabase {
    private database: any;

    constructor(database: any) {
        this.database = database;
    }

    public async setData(path: string, data: any): Promise<void> {
        await this.database.ref(path).set(data);
    }

    public async getData(path: string): Promise<any> {
        const snapshot = await this.database.ref(path).once('value');
        return snapshot.val();
    }
}