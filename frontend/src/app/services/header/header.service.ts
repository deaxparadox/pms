import { HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class HeaderService {
  options = {
    headers: new HttpHeaders()
  }

  private generate_token(token: string): string {
    return `Token ${token}`
  }

  set(key: string, token: string): HttpHeaders {
    return this.options.headers.set(key, this.generate_token(token))
  }

}
