import { Component, OnInit } from '@angular/core';

import { Task } from './config.service';
import { HeadingService } from './heading.service';
import { Heading } from './heading';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  task: Task | undefined;

  title = 'frontend';

  constructor(private httpClientHeading: HeadingService) {}

  headings?: Heading[];

  ngOnInit(): void {
    this.httpClientHeading.getHeadings().subscribe(headings => {
      console.log(headings)
      this.headings = headings
    });
  }

  showTask() {
    // this.configService.
  }
}
