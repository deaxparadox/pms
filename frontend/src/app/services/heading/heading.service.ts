import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Heading, HeadingWithTasks } from '../../heading';
import { HeaderService } from '../header/header.service';
import { LoginService } from '../login/login.service';
import { Token } from '@angular/compiler';
import { UserToken } from '../login/token';


// const httpOptions = {
//   headers: new HttpHeaders({
//     Authorization: `Token 9fe56e05951440d9e4accc2f84d3b368aedbbdd0`
//   })
// }

@Injectable({
  providedIn: 'root'
})
export class HeadingService implements OnInit {
  
  constructor(
    private httpClient: HttpClient,
    private headerService: HeaderService,
    private loginService: LoginService
  ) { }

  ngOnInit(): void {
  }

  user_token?: UserToken;

  getHeadings(): Observable<Heading[]> {
    // this.httpOptions.options.headers = this.user();
    // this.loginService.login<UserToken>().subscribe(async (user) => {
    //   this.user_token = user;
    //   console.log(this.user_token)
    // })
    
    this.headerService.options.headers = this.user("9fe56e05951440d9e4accc2f84d3b368aedbbdd0")
    return this.httpClient.get<Heading[]>(
      "http://localhost:8000/api/v1/", this.headerService.options
    )
  }

  user(token: string): HttpHeaders {
    return this.headerService.set("Authorization", token);
  }

  getHeading(id: number): Observable<HeadingWithTasks> {
    return this.httpClient.get<HeadingWithTasks>(`http://localhost:8000/api/v1/heading/${id}/`)
  }
}
