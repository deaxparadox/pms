import { Component, OnInit } from '@angular/core';

import { Task } from './config.service';
import { HeadingService } from './services/heading/heading.service';
import { Heading } from './heading';
import { HttpClient } from '@angular/common/http';
import { LoginService } from './services/login/login.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],

})
export class AppComponent implements OnInit{
  task: Task | undefined;

  title = 'frontend';

  constructor(
    private httpClientHeading: HeadingService,
    private httpClient: HttpClient,
    private loginService: LoginService,
    private router: Router
  ) {}

  headings?: Heading[];

  ngOnInit(): void {
    this.httpClientHeading.getHeadings().subscribe(headings => {
      console.log(headings)
      this.headings = headings
    });

    if (!this.loginService.user_token) {
      this.router.navigate(['/login']);
    } 
  }

  showTask() {
    // this.configService.
  }
}
