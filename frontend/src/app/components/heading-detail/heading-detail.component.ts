import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HeadingWithTasks } from 'src/app/heading';
import { HeaderService } from 'src/app/services/header/header.service';
import { HeadingService } from 'src/app/services/heading/heading.service';
import { TaskService } from 'src/app/services/task/task.service';




@Component({
  selector: 'app-heading-detail',
  templateUrl: './heading-detail.component.html',
  styleUrls: ['./heading-detail.component.css']
})
export class HeadingDetailComponent implements OnInit{
  constructor(
    private route: ActivatedRoute,
    private httpHeadingService: HeadingService
  ) { }

  ngOnInit(): void {
      console.log(this.route.snapshot.paramMap.get("id"));
      this.getHeading();
  }

  heading?: HeadingWithTasks;

  getHeading() {
    let headingId = Number(this.route.snapshot.paramMap.get("id"));
    this.httpHeadingService.getHeading(headingId).subscribe(
      heading => {
        
        this.heading = heading;
        console.log(this.heading);
      }
    )
  }

}
