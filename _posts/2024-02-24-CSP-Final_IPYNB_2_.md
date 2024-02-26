---
title: CSP Final
categories: ['CSP', 'Week 21']
tags: ['hacks']
---

# Individual Review

Filler.

# Team Review

## Features Prior to Implementation

Description of features prior to implementation:



* Design and planning
* Key features
* [Features prior to implementation](https://kinetekenergy.github.io/blog/posts/Checkpoint_IPYNB_2_/)

Planning table of issues and features:

Features:

<table>
  <tr>
   <td><strong>Features</strong>
   </td>
   <td><strong>Link</strong>
   </td>
  </tr>
  <tr>
   <td>View count which updates whenever someone views a video
   </td>
   <td rowspan="5" ><a href="https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3">Issue</a>
   </td>
  </tr>
  <tr>
   <td>Video categories to sort videos and choose which category to watch
   </td>
  </tr>
  <tr>
   <td>Login feature which connects to upload. When uploading a video, the user who uploaded it will be in the description and this will be automatic.
   </td>
  </tr>
  <tr>
   <td>Deleting user accounts and updating an email so that users can close their account and update information
   </td>
  </tr>
  <tr>
   <td>Allow users to add a description to their videos. They can also add a tag so that the category feature sorts it
   </td>
  </tr>
</table>



|Issue|Solution|
|-|-|
|View counter was not updating|The HTML request had to be a `1PUT` so that it could update the view count. It should then commit to `db` with `db.commit()`. [Fix](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/240de7cd9cf8040637bb87eec5bf8264565cab1b) & [Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3)|
|Return errors were all messed up and weren’t returning the correct error code (this error actually showed up during a live review but was fixed on-the-fly).|The `return` code allows you to choose the error. This needed to be set properly because we had messed up the codes. [Fix](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/6352cfac8f3f499751d44ce573be3aadc324f4fb) & [Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-blog/issues/3)|
|Adding a video would be NULL and the video id in the URL wouldn’t work.|Code was reordered so that the video id was put properly: `self._videoID = self.id` was changed to be last so that the video id is updated last and isn’t changed. [Fix](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/00f2e4a3f99cea3a05d50674e7b41cafccd83410) & [Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/00f2e4a3f99cea3a05d50674e7b41cafccd83410)|
|Users could add random text for emails and junk text.|A filter was added so that emails must contain an “@” symbol as well as being over five characters. [Fix](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/29073c9a91fa89dc4b7ab29a261e13d296cda4a3) & [Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/00f2e4a3f99cea3a05d50674e7b41cafccd83410)|
|Video thumbnails were not working.|The image in the backend is stored as a base64 and is sent to the front end. However, there were issues in the javascript decoding. To fix this, a `regex` was implemented so that the base64 is cleaned up and is displayed properly. [Fix](https://github.com/Napoleon-Bonaparte-Official/corsica-frontend/commit/bbce2f295fe3414cd2a97ae3b756fe65d57ffc87) & [Issue](https://github.com/Napoleon-Bonaparte-Official/corsica-backend/commit/00f2e4a3f99cea3a05d50674e7b41cafccd83410)|


