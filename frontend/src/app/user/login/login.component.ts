import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from 'src/app/services/login/login.service';
import { UserToken } from 'src/app/services/login/token';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  constructor(
    private loginService: LoginService,
    private router: Router
  ) {}
  
  
  invalid_username_password_status: boolean = false;
  invalid_username_password_message = "Invalid username or password!"

  login(username: string, password: string) {
    if ((!username) || (!password)) {
      console.log("Invalid username or password!:(");
      this.invalid_username_password_status = true;
      return

    }

    this.invalid_username_password_status = false;

    this.loginService.login<UserToken>(username, password).subscribe(
      (t) => {
        this.loginService.user_token = t.token;
        console.log(this.loginService.user_token)
      }
    )

    if (this.loginService) {
      this.router.navigate(['dashboard/']);
    }
  }

  login_on_enter(event: KeyboardEvent, username: string, password: string) {
    event.preventDefault();
    console.log(event);
    // if (event.key === 'enter') {
    //   this.login(username, password);
    // }
  }

}
