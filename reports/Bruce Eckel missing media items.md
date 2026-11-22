# Media page omits 37 public items

The media page at `content/media/index.md` lists 34 links,
and the research found **37 further entries** that belong on it:
19 conference and company talks, 8 podcast and video interviews, and 10 written interviews, reviews, and article collections.
Seven of them have a video page that a fetch confirmed as live: PyCon US 2013, PyCaribbean 2017, the JET Conference 2015 keynote, CRAFT Conference 2014, the January 2026 GOTO Book Club interview, the November 2025 Bootiful Podcast video, and the June 2026 PyCharm interview recorded at PyCon US 2026.
The page also carries **8 dead links**, 3 links that redirect to a new address, and 2 links that block automated clients.
Five of the eight dead links have a replacement confirmed by fetch.
The OSCON and Heroku links each have a candidate that needs a look in a browser, and the VJug24 keynote has no replacement.
The largest gaps are the 2001 to 2009 Python keynotes, the 2012 to 2015 European conference run, and everything after PyCon US 2024.
A further set of items is unconfirmed and sits in its own section at the end, including the recording of the May 2026 PyCon US talk "Demystifying the GIL", which no search located.
All checks ran on 2026-11-22.

Each table below gives a status for its URL.
"Fetched" means a researcher fetched the page that day and its content matched the item.
"Not fetched" means the URL came from a search result or from a link on another fetched page.
A fetch of a YouTube page confirms that the page is live and what its title is; it cannot confirm that the video still plays.

## Four missing talks have a live recording, and fifteen have slides or a report

The Python talks fall in three clusters:
keynotes from 2001 to 2009, two talks in 2013 and 2017, and the PyCon US run from 2022 to 2026.
The page covers three talks of the third cluster and none of the first two.
pyvideo.org lists five talks under his name, and two of those are absent from the page ([pyvideo.org](https://pyvideo.org/speaker/bruce-eckel.html)).
The non-Python talks follow a similar pattern:
the page has the 2019 GeeCON slides and the 2022 talks,
while the 2012 to 2015 appearances in Poznan, Budapest, Prague, and Minsk are missing.

These four talks have a recording to link.

| Date | Title | Venue | URL | Status |
|---|---|---|---|---|
| February 2017 | Science is What Works (keynote) | PyCaribbean 2017, Puerto Rico | https://www.youtube.com/watch?v=_ncc69-cunA | Fetched; page title is "Bruce Eckel - Keynote". The talk title comes from [his blog post](https://bruceeckel.com/2017/04/19/pycaribbean-keynote-on-youtube/), fetched |
| September 2015 | A Language is More Than a Language (opening keynote) | JET Conference, Minsk, Belarus | https://www.youtube.com/watch?v=d25z-wO1zzs | Fetched; title matches, channel jetconf. [His video post](https://bruceeckel.com/2016/01/10/video-of-belarus-conference-opening-keynote/) was fetched too |
| 2014 (published August 2014) | What Makes a Good Development Process? | CRAFT Conference 2014, Budapest | https://www.infoq.com/presentations/development-patterns-process/ | Fetched; 46:20 recording. The talk month is not on the page |
| March 2013 | Rethinking Errors: Learning from Scala and Go | PyCon US 2013, Santa Clara | https://www.youtube.com/watch?v=REOL1AV_PCg | Fetched; title matches. The [pyvideo.org entry](https://pyvideo.org/pycon-us-2013/rethinking-errors-learning-from-scala-and-go.html) was fetched and points at this video |

The next fifteen entries have no recording that the research found.
The URL in each row is the best live page: a schedule entry, a slide deck, or a contemporary report.

| Date | Title | Venue | URL | Status |
|---|---|---|---|---|
| May 2026 | Demystifying the GIL | PyCon US 2026, Long Beach | https://us.pycon.org/2026/schedule/presentation/45/ | Fetched; schedule page, no video link. Materials at https://github.com/BruceEckel/DemystifyingTheGIL, not fetched |
| Fall 2024 | Effect Oriented Programming (with Bill Frasure and James Ward) | dev2next 2024, Denver area | https://effectorientedprogramming.github.io/presos/dev2next_2024 | Fetched; slides. The event name comes from the URL path, and the dates (September 30 or October 1 to October 3) from unfetched listings |
| September 2015 | Creating Trust Organizations (evening talk before the conference) | JET Conference, Minsk, Belarus | https://bruceeckel.com/2015/09/24/jet-conference-slides/ | Fetched; the post links Google Slides for this talk and for the keynote. The Slides links were not fetched |
| April 2015 | The Next Big Challenge: Getting Better Ideas | Company talk at VuWall, Montreal | https://bruceeckel.com/2015/05/04/getting-better-ideas-presentation/ | Fetched; blog post. Its recording, https://www.youtube.com/watch?v=6DYLJGwrTo0, returned no title, so the video is possibly private or removed |
| January 2015 | Phase 3: Better Ideas | Company talk at Salesforce | https://www.slideshare.net/slideshow/phase-3-better-ideas-presentation-at-salesforce-1282015/44013187 | Not fetched; the deck is listed on his [SlideShare profile](https://www.slideshare.net/bruceeckel), which was fetched |
| October 2014 | Do Languages Matter? (closing talk) | GeeCON Prague 2014 | https://www.slideshare.net/slideshow/do-languages-matter/40681551 | Fetched; first slide gives event, date (October 24), and city |
| May 2012 | The Power of Hybridization; Reinventing Business; Atomic Scala (seminar) | GeeCON 2012, Poznan, Poland | https://2012.geecon.org/speakers/bruce-eckel/ | Fetched; speaker page lists all three sessions |
| June/July 2009 | Keynote on software archeology (exact title not found) | EuroPython 2009, Birmingham, UK | https://ep2009.europython.eu/ | Fetched; names him as keynote speaker. The topic comes from an [attendee post](https://wordaligned.org/articles/europython-2009), fetched. The two blip.tv recordings are gone |
| November 2008 | Open Space introduction and facilitation | QCon San Francisco 2008 | https://qconsf.com/sf2010/sf2008/speaker/Bruce%2bEckel.html | Fetched |
| September 2008 | Why I Love Python; Burning Man (two talks) | PyConBrasil 2008, Rio de Janeiro | https://www.serpro.gov.br/menu/noticias/noticias-antigas/a-vida-e-curta-logo-use-python | Fetched; news item in Portuguese, the single source |
| January 2007 | Keynote (title not found; on dynamic languages and failing fast) | CodeMash 2007 | https://www.blueskyonmars.com/2007/01/18/bruce-eckels-codemash-keynote-on-a-dynamic-world | Fetched; attendee write-up |
| March 2005 | Object-Oriented Design with Python | PyCon DC 2005, Washington DC | https://pycon.blogspot.com/2005/03/afternoon-talks.html | Fetched; official PyCon blog recap. [Ted Leung's session notes](https://www.sauria.com/twl/conferences/pycon2005/20050323/Object-Oriented%20Design%20with%20Python.html) were fetched too |
| June 2004 | Java Issues & Directions | UC Berkeley, Haas School of Business | https://www.osnews.com/?p=7646 | Fetched; news post. The RealMedia stream it links is almost certainly dead |
| March 2004 | How to Argue About Types (keynote) | PyCon DC 2004, Washington DC | https://www.linuxjournal.com/article/7541 | Fetched; conference report. The title rests on one [attendee post](https://yergler.net/2004/03/26/pycon-day-3/), fetched |
| March 2001 | Why I Love Python (closing keynote) | Ninth International Python Conference, Long Beach | https://www.slideshare.net/slideshow/why-i-love-python/493670 | Fetched; third-party upload of his 2001 slides. The [Linux Journal report](https://www.linuxjournal.com/article/4731) of the keynote was fetched and omits the title |

Two details in this group need care when you write the entries.
The IPC9 title is assembled from two sources: the slides carry the title and a 2001 copyright, and Linux Journal places the "top ten reasons" keynote at the conference.
The PyCaribbean talk took place on February 18, 2017, and April 19, 2017 is the date of the blog post that announced the video.

The research also checked years that produce no entry.
The PyCon US 2025 talks list has no talk of his ([PyCon archive](https://pycon-archive.python.org/2025/schedule/talks/)),
and at PyCon 2016 he ran two open spaces and gave no talk ([bruceeckel.com](https://bruceeckel.com/2016/06/15/pycon-2016/)).

## Eight podcast and video interviews are missing, four of them since 2024

The page stops at July 2022 for interviews.
Since then he has appeared twice on Josh Long's A Bootiful Podcast,
once on the GOTO Book Club with his *Effect Oriented Programming* co-authors,
and once on the PyCharm channel in a conversation with Paul Everitt recorded at PyCon US 2026.
The PyCharm interview is the one item that centers on his current Python work.
The older misses are two Java Posse episodes beyond the two the page has, a 2019 episode of The 6 Figure Developer, and a 2008 episode of The Flex Show.

| Date | Title | Venue | URL | Status |
|---|---|---|---|---|
| June 2026 | Bruce Eckel on Free-Threaded Python, Type Checking, and Programming in the AI Era (interviewer Paul Everitt, recorded at PyCon US 2026) | PyCharm YouTube channel | https://www.youtube.com/watch?v=hj6RiSEUuoY | Fetched; title, channel, and upload date 2026-06-17 confirmed |
| January 2026 | Effect Oriented Programming (with Bill Frasure and James Ward; interviewer Andrew Harmel-Law) | GOTO Book Club | https://gotopia.tech/episodes/420/effective-oriented-programming | Fetched; published 2026-01-22. Video at https://www.youtube.com/watch?v=Qds6rO9lxps, fetched. The audio feed released it on February 24, 2026 |
| November 2025 | The legendary Bruce Eckel on language design, effects, abstraction, concurrency, and so much more (host Josh Long) | A Bootiful Podcast | https://spring.io/blog/2025/11/13/a-bootiful-podcast-bruce-eckel/ | Fetched. The [Podbean episode page](https://bootifulpodcast.podbean.com/e/the-legendary-bruce-eckel-on-language-design-effects-abstraction-concurrency-and-so-much-more/) and the video at https://www.youtube.com/watch?v=h1MGDpJVj4s were fetched too |
| October 2024 | Bruce Eckel, 'Thinking in Java' author and one of the most influential authors in my career (host Josh Long, recorded at dev2next) | A Bootiful Podcast | https://bootifulpodcast.podbean.com/e/bruce-eckel-thinking-in-java-author-and-one-of-the-most-influential-authors-in-my-career | Fetched; published October 3, 2024 |
| September 2019 | Episode 111: Atomic Kotlin and Teal Orgs with Bruce Eckel | The 6 Figure Developer Podcast | https://6figuredev.com/podcast/episode-111-atomic-kotlin-and-teal-orgs-with-bruce-eckel/ | Fetched; published September 30, 2019 |
| May 2014 | #454: Roundup '14 - Alternative Organization Structures | The Java Posse | http://javaposse.com/java-posse-454 | Fetched over plain http; the site has no working https. The show notes link his name and Reinventing Business and list no speakers |
| August 2008 | Episode 50: Interview: James Ward and Bruce Eckel | The Flex Show | https://jamesward.com/2008/08/15/flex-show-with-bruce-eckel | Fetched; James Ward's announcement. The show's own episode page is dead, and its Wayback snapshot came back nearly empty |
| July 2007 | #131: Walking Around JavaOne 2007 - Part 2 (segment "Bruce Eckel and Mindview") | The Java Posse | http://javaposse.com/java_posse_131_walking_around_java_one_2007_part_2 | Fetched over plain http |

A month-by-month scan of the Java Posse archive from 2005 through 2015 found him as a participant in four episodes: #036 and #037, which the page has, and #131 and #454 ([javaposse.com](http://javaposse.com/java-posse-454)).
The show notes of the Roundup session episodes list no participants, so other recordings that contain his voice cannot be attributed from text.
Two search hits look like appearances and are mentions.
Python Bytes #493 names his free book *Thinking in Python* in its Extras ([pythonbytes.fm](https://pythonbytes.fm/episodes/show/493/x)),
and Talk Python #149 does not feature him; his one Talk Python episode is #148, which the page has.
Searches for about thirty other shows, among them Software Engineering Radio, CppCast, Talking Kotlin, and Test and Code, returned no episode with him as a guest.
That evidence is weaker than the Java Posse scan, since no show's own search was run.

## Ten written pieces are missing, led by three parts of the 2003 Artima conversation

The page links Part I of Bill Venners's four-part Artima conversation and omits Parts II through IV.
Part IV announces a different interviewee for the next installment, so the series has four parts ([Artima](https://www.artima.com/intv/tippingP.html)).
The other written misses are a 2003 Borland interview, a Japanese translation of the 2009 InfoQ interview, three pieces of book coverage from 2000 to 2006, one 2026 article about *Thinking in Python*, and his Artima weblog.

| Date | Title | Venue | URL | Status |
|---|---|---|---|---|
| August 2026 | Thinking in Python: Bruce Eckel Revives His 2008 Book With Claude in 2026 | Developers Digest | https://www.developersdigest.tech/blog/thinking-in-python-bruce-eckel-2026 | Fetched; dated August 24, 2026. Small outlet, no author named |
| May 2009 | Bruce Eckel氏、Python、Java、Flex、RIAについて語る (Japanese translation of the InfoQ interview on the page) | InfoQ Japan | https://www.infoq.com/jp/news/2009/05/bruce-eckel/ | Fetched |
| April 2006 | Thinking in Java, new 4th Ed. (review by Dr Pan Pantziarka) | The Register | https://www.theregister.com/software/2006/04/07/thinking-in-java-new-4th-ed/683565 | Fetched |
| July 2003 | Python and the Tipping Point: A Conversation with Bruce Eckel, Part IV | Artima Developer | https://www.artima.com/intv/tippingP.html | Fetched; dated July 21, 2003. The newer address https://www.artima.com/articles/python-and-the-tipping-point returns 200, content not read |
| July 2003 | Type Checking and Techie Control: A Conversation with Bruce Eckel, Part III | Artima Developer | https://www.artima.com/articles/type-checking-and-techie-control | Fetched; dated July 7, 2003 |
| July 2003 (approximate) | Interview with Bruce Eckel by Clay Shannon | Borland Developer Network | http://web.archive.org/web/20080517031942/http://community.borland.com/article/0,1410,30139,00.html | Fetched with curl; Wayback copy, the original is gone. The month comes from two blog posts that link to it, dated July 22 and July 31, 2003 |
| June 2003 | The Zen of Python: A Conversation with Bruce Eckel, Part II | Artima Developer | https://www.artima.com/articles/the-zen-of-python | Returns 200, content not read. The same article was fetched at the older address https://www.artima.com/intv/prodperf.html, dated June 23, 2003 |
| June 2003 | The 13th Annual Software Development Jolt & Productivity Awards (lists *Thinking in Java*, 3rd edition) | Software Development magazine, archived by Dr. Dobb's | http://web.archive.org/web/2023/https://www.drdobbs.com/joltawards/the-13th-annual-software-development-jol/184414991?pgno=7 | Fetched with curl; Wayback copy, the live address no longer resolves. The excerpt does not say whether the book won the Jolt or a Productivity Award |
| April 2000 | Thinking in Java (review by Jeff Berry of the first edition) | LWN.net | https://static.lwn.net/Reviews/ThinkingInJava.php3 | Fetched; dated April 22, 2000 |
| About 2003 to November 2014 | Computing Thoughts: A Weblog by Bruce Eckel | Artima Developer weblogs | https://www.artima.com/weblogs/index.jsp?blogger=beckel | Fetched; 19 index pages of 15 posts, the last dated November 21, 2014. The start year is an estimate |

The Artima interview index dates the conversation August 2002, and each article page carries a June or July 2003 date ([Artima](https://www.artima.com/articles/type-checking-and-techie-control)).
The article dates match the Part I entry on the page, so use them.
Written coverage after 2022 is thin.
The Developers Digest article is the one independent written piece from 2023 to 2026,
and no written review of *Effect Oriented Programming* turned up anywhere.

## Eight links on the page are dead, and five have a confirmed replacement

A check of all 34 URLs found 8 that fail or land on a generic page.
InformIT has retired its old article addresses, JavaWorld has folded into InfoWorld, and Stitcher has closed.

| Entry on the page | What the link does now | Replacement | Status |
|---|---|---|---|
| February 2021, Interview on Frontmatter Podcast (stitcher.com) | Redirects to a Pandora "stitcher-sunset" page | https://leanpub.com/podcasts/leanpub/bruce-eckel-02-02-21 (audio and full transcript); video at https://www.youtube.com/watch?v=rtSl-N6li8Y | Both fetched |
| November 2017, VJug24 keynote (virtualjug.com) | Connection fails | None found; no Wayback snapshot and no YouTube copy turned up | No replacement |
| June 2015, Creating Trust Organizations (conferences.oreilly.com) | Redirects to the generic O'Reilly conferences page | http://web.archive.org/web/20191120193433/https://conferences.oreilly.com/oscon/open-source-2015/public/schedule/detail/41505 | Not fetched; the Wayback API reports a snapshot, content unread |
| 2013, Interview with James Ward (lightbend.com) | 404 | http://web.archive.org/web/20150907021510/https://www.typesafe.com/blog/bruce-eckel-on-learning-scala-and-tech-conferences | Fetched with curl; dated July 8, 2013, a written interview |
| May 2012, Reinventing Business Presentation at Heroku (vimeo.com review link) | 404 | https://vimeo.com/40551380 | Returns 200 with an empty title; check in a browser |
| May 2007, Is This the Best We Can Do? (informit.com) | Redirects to the InformIT articles index | http://web.archive.org/web/20250513191100/https://www.informit.com/articles/article.aspx?p=762675 | Fetched with curl; dated May 18, 2007 |
| Sept 2001, InformIT interview (informit.com) | Redirects to the InformIT articles index | http://web.archive.org/web/20250326021354/https://www.informit.com/articles/article.aspx?p=23416 | Fetched with curl; dated September 21, 2001 |
| June 2001, Thinking in Java Interview (javaworld.com) | Redirects to the InfoWorld home page | https://www.infoworld.com/article/2161387/eckel-thinks-in-java.html | Fetched; "Eckel thinks in Java", John Zukowski, June 8, 2001 |

Three links work and redirect to an address worth writing into the file.
Each new address returned 200, and no researcher read its content.
The Eric Gunnerson interview is now at https://learn.microsoft.com/en-us/archive/blogs/ericgu/insights-into-the-net-architecture.
The Rethinking Scala deck is at https://www.slideshare.net/slideshow/rethinking-scala-presented-in-san-francisco-may-7-2014/34401420.
PyDev of the Week is at https://blog.pythonlibrary.org/2017/11/06/pydev-of-the-week-bruce-eckel/.

Two Oracle links return 403 to automated clients and need a browser check:
the Java Magazine author page and the September 2017 review of *On Java 8*.
Wayback holds a March 2026 snapshot of the author page ([Wayback](http://web.archive.org/web/20260310125409/https://blogs.oracle.com/authors/bruce-eckel/)), so the page existed eight months ago.
The remaining 21 links return 200.
Nine of those are YouTube links, and YouTube returns 200 for a removed video, so a click on each is the reliable test.
The WeChat link for the Chinese InfoQ interview often shows a verification page to non-browser clients and deserves the same click.

The research also turned up corrections to entries that stay.
The link text "InforIT Interview" is a typo for "InformIT".
The Geecon 2019 slides entry has no title, and the talk is "Three Programming Disruptions" ([bruceeckel.com](https://bruceeckel.com/2019/08/29/three-programming-disruptions/)).
The opensource.com interview is labeled June 2015 while its URL path says July 2015; no researcher fetched the page to settle the month.
The May 2014 Rethinking Scala talk was an SF Scala meetup at Chartboost ([Meetup](https://www.meetup.com/sf-scala/events/179263772)).

## Unconfirmed items need a browser or a listen before they go on the page

These items surfaced in the research and lack one piece of confirmation.
None of them belongs on the page until that piece is checked.

| Item | What is known | What is missing |
|---|---|---|
| Recording of "Demystifying the GIL", PyCon US 2026 | The talk is confirmed; the schedule page has no video link | A video URL. Check the PyCon US YouTube channel and pyvideo.org by hand |
| "Open Spaces Introduction (by Bruce Eckel)", https://www.youtube.com/watch?v=aD3S0wlbek0 | Fetched; channel Douglas Napoleone, uploaded 2009-01-09 | The event and date of the recording |
| "Reinventing Business: Audacity and Humility", https://www.slideshare.net/slideshow/reinventing-business-audacity-and-humility/40549864 | Deck fetched; uploaded next to the GeeCON Prague deck, which suggests October 2014 | The event; the deck names none |
| "The Eckel Index: New language features from Java 9 through Java 17", Java Magazine, July 2022, https://blogs.oracle.com/javamagazine/post/java-eckel-index | Search snippet; a Wayback snapshot exists. It indexes his seven 2022 articles and would be a better link than the author page | Oracle returns 403, so title, date, and content are unread |
| "Why Learn Kotlin?", JetBrains Kotlin blog, April 2021, https://blog.jetbrains.com/kotlin/2021/04/why-learn-kotlin/ | Returns 200; a search snippet says it features *Atomic Kotlin* | Title, author, and date; the fetch got 403 |
| "Atomic Kotlin Review", https://griffio.github.io/kotlin/2021/02/12/Atomic-Kotlin-Review | Search result; a reader's personal blog | Not fetched, and not a notable publication |
| EuroPython 2009 keynote title and recordings | Two recordings were listed under his name on blip.tv, which shut down in 2015 ([europython list](https://mail.python.org/pipermail/europython/2009-July/007488.html)) | The exact title, whether he gave one session or two, and a live host for the video |
| The Flex Show episode 50 audio | James Ward's announcement is live | A working episode page or audio file |
| Panel on entering computer science as a new graduate, Western, Gunnison, September 11, 2025, with Bill Venners and Dianne Marsh | Released as Happy Path Programming #117, his own podcast, which the page links as a whole; slides possibly at https://github.com/BruceEckel/WU | The episode page was not fetched |
| Possible talk at ICALEPCS 2011, Grenoble | An author-index URL in search results, https://accelconf.web.cern.ch/icalepcs2011/html/auth0336.htm | Not fetched; no talk confirmed |
| "Effect-Oriented Programming" on saltmarch.com | A page in search results | The speaker; it is possibly James Ward alone |
| JavaPolis Flex keynote with James Ward and Christoph Rooms | Described in a James Ward post, not fetched | Parleys is offline, so no live video URL |
| Java Posse interviews at Devoxx 2008 and 2009 | One search summary claimed them | The javaposse.com scan contradicts the claim; treat it as wrong |
| Software Development Conference and JavaOne sessions | Bios state that he chaired the C++ and Java tracks | No session records online |
| Adapters and Interfaces sprint coach, PyCon 2005 era | A wiki page in search results | Not fetched, not dated |

Several negative results are weak and worth knowing.
The search tool handles non-English queries poorly, so the absence of Chinese, Russian, Polish, and Portuguese interviews is "not found".
GeeCON's Vimeo channel was not paged through for the 2012, 2014, and 2019 talks.
The Internet Archive was not searched for the 2004 Haas stream or for magazine scans.

## Conclusion

The missing entries change what the page says about his career.
With them it shows a Python keynote speaker from 2001 onward, a business-organization thread that runs from Heroku in 2012 through Salesforce, VuWall, and Minsk in 2015, and a current phase built on *Effect Oriented Programming* and free-threaded Python.
Without them the page reads as a Java author who came to Python talks in 2022.

Link decay is the larger maintenance problem.
Nearly a quarter of the page's links have died, and three sources of loss (InformIT, JavaWorld, Stitcher) each took several years to fail.
The entries that survive best point at a publisher's own episode page or at a Wayback snapshot, so each new entry is safer with one of those than with an aggregator link.
The remaining work is manual and short: click the nine YouTube links and the two Oracle links, find the PyCon US 2026 video, and listen to Java Posse #454 to confirm his role.
