import { HttpClient } from '@angular/common/http';
import { Token } from '@angular/compiler';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(
    private httpClient: HttpClient,
  ) { }

  user_token?: string;
    
  login<T>(username: string, password: string): Observable<T> {
    return this.httpClient.post<T>("http://localhost:8000/api/login/", {
      username: username,
      password: password,
    });
  }

  invalid_username_password_status: boolean = true;
  invalid_username_password_message = "Invalid username or password!"
}
