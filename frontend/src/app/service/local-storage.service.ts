import {Injectable} from '@angular/core';
import {User} from "./interfaces/user";

@Injectable({
  providedIn: 'root'
})
export class LocalStorageService {

  private storage: Storage;
  constructor() {
    this.storage = window.localStorage;
  }

  set(key: string, value: any) {
    if(!this.storage) {
      alert('Local storage not supported by your browser.');
      return false;
    } else {
      this.storage.setItem(key, JSON.stringify(value));
      return true;
    }
  }

    get(key: string): any {
    if (this.storage) {
      return JSON.parse(this.storage.getItem(key) || '{}');
    }
    return null;
  }

  remove(key: string): boolean {
    if (this.storage) {
      this.storage.removeItem(key);
      return true;
    }
    return false;
  }

  clear(): boolean {
    if (this.storage) {
      this.storage.clear();
      return true;
    }
    return false;
  }
}
