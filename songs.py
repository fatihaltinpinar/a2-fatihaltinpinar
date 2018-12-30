def songs(comments):
    # noinspection PyStringFormat
    print('all comments =', comments)
    comment_list = '<ul>'

    # for comment in comments:
    # Added for list access
    for i in range(len(comments)):
        comment = comments[i]
        comment_list = comment_list + '<li><span class="username">{}</span>'.format(comment['username'])
        comment_list = comment_list + '<span class="time">Sent on {:%H:%M:%S %d/%m/%y} </span>'.format(comment['time'])
        comment_list = comment_list + '<div class="commentText">{}</div></li>'.format(comment['commentText'])

        # comment_list += '<li><strong>{}</strong> said at {:%H:%M:%S %d/%m/%y} </br> {}</li>'.format(comment['username'],
        #                                                                                             comment['time'],
        #                                                                                             comment['commentText'])

    comment_list = comment_list + '</ul>'

    page = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Songs of the Branches</title>
	<meta charset="utf-8"/>


	<link rel="stylesheet" type="text/css" href="css/style.css"/>
	<link rel="stylesheet" type="text/css" href="css/songs.css"/>

	<meta name="description" content="This is a fan website for the post-rock group: &quot; IF THESE TREES COULD TALK&quot;">
	<meta name="keywords" content="IF THESE TREES COULD TALK, Red Forest, Above the Earth Below the Sky, The Bones of a Dying World, Post Rock">
	<meta name="author" content="Fatih Altınpınar">
	<link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />

</head>
<body>
	<div class="container">
		<!-- navigation -->

		<header>
			<div class="navBar">
				<a href="/" class="navImg">
						<img src="img/logo.svg" alt="Tree Logo">
				</a>
				<div class="navLinks">
					<a href="/">HOME</a>
					<a href="about.html">ABOUT</a>
					<a href="members.html">MEMBERS</a>
					<a class="active" href="songs.html">SONGS</a>
					<!--<a href="source.html">SOURCES</a>-->
				</div>
			</div>
		</header>


		<div class="content">
			<table>

				<!-- Table Headers -->
				<tr>
					<th class="tableBigHeader" colspan="4" >Songlist</th>
				</tr>
				<tr>
					<th>Album</th>
					<th>Song</th>
					<th>Lenght</th>
					<th>Listen the Songs!</th>
				</tr>


				<!-- IF These trees could talk album-->
				<tr>
					<td>If These Trees Could Talk</td>
					<td>Malabar Front</td>
					<td>08:05</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=3447102285/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td rowspan="5"><img class="albumCover" src="img/album_if_these_trees_could_talk.jpg" title="If These Trees Could Talk"></td>
					<td>Smoke Stacks</td>
					<td>06:24</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=3447102285/size=small/bgcol=333333/linkcol=0687f5/artwork=none/track=3080452033/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>The Friscalating Dusklight</td>
					<td>04:32</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=3447102285/size=small/bgcol=333333/linkcol=0687f5/artwork=none/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Signal Tree</td>
					<td>05:24</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=3447102285/size=small/bgcol=333333/linkcol=0687f5/artwork=none/track=4165959542/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>The Death of Paradigm</td>
					<td>04:06</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=3447102285/size=small/bgcol=333333/linkcol=0687f5/artwork=none/track=1139349099/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Signal Tree</td>
					<td>05:24</td>
					<td>
						<iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=3447102285/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=1072315996/transparent=true/"></iframe>
					</td>
				</tr>
				


				<!-- Above the earth, below the sky album-->
				<tr>
					<td>Above The Earth, Below the Sky</td>
					<td>From Roots To Needles</td>
					<td>06:42</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=798581289/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=3713287390/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td rowspan="9"><img class="albumCover" src="img/album_above_below.jpg" title="Above the Earth, Below the Sky"></td>
					<td>What's in the Ground Belongs to You</td>
					<td>04:14</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=798581289/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=294391939/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Terra Incognita</td>
					<td>00:57</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=798581289/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=3228883329/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Above The Earth</td>
					<td>02:19</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=798581289/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=2974510417/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Below The Sky</td>
					<td>07:20</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=798581289/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=4111175018/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>The Sun Is In The North</td>
					<td>05:45</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=798581289/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=3609824515/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Thirty-Six Silos</td>
					<td>04:39</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=798581289/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=594999479/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>The Flames of Herostratus</td>
					<td>05:34</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=798581289/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=3339144798/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Rebuilding The Temple Of Artemis</td>
					<td>05:05</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=798581289/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=294763036/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Deus Ex Machina</td>
					<td>02:23</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=798581289/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=1367365649/transparent=true/"></iframe></td>
				</tr>


				<!-- Red Forest -->

				<tr>
					<td>Red Forest</td>
					<td>Breath Of Life</td>
					<td>01:48</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=1591277760/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=3073233405/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td rowspan="8"><img class="albumCover" src="img/album_red_forest.jpg" title="Red Forest"></td>
					<td>The First Fire</td>
					<td>06:30</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=1591277760/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=1000402672/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Barren Lands of the Modern Dinosaur</td>
					<td>05:57</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=1591277760/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=411208920/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>They Speak With Knives</td>
					<td>02:19</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=1591277760/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=3706636867/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>The Gift of Two Rivers</td>
					<td>01:11</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=1591277760/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=1320506243/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Red Forest</td>
					<td>08:25</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=1591277760/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=2404839061/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Aleustian Clouds</td>
					<td>03:03</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=1591277760/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=2291579666/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Left To Rust and Rot</td>
					<td>05:24</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=1591277760/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=3623801648/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>When The Big Hand Buries The Twelve</td>
					<td>09:38</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=1591277760/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=2999786822/transparent=true/"></iframe></td>
				</tr>
				

				<!-- The Bones of a Dying World -->

				<tr>
					<td>The Bones of a Dying World</td>
					<td>Solstice</td>
					<td>07:49</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=4236207006/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=1605386968/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td rowspan="8"><img class="albumCover" src="img/album_bones.jpg" title="The Bones of a Dying World"></td>
					<td>Swallowing Teeth</td>
					<td>04:27</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=4236207006/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=3501067683/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Earth Crawler</td>
					<td>06:38</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=4236207006/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=1532516274/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>After the Smoke Clears</td>
					<td>06:18</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=4236207006/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=892139913/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>The Here and Hereafter</td>
					<td>02:33</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=4236207006/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=756450468/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Iron Glaicer</td>
					<td>08:25</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=4236207006/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=3569871795/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>The Giving Tree</td>
					<td>06:03</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=4236207006/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=2152619477/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>Berlin</td>
					<td>04:44</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=4236207006/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=90117021/transparent=true/"></iframe></td>
				</tr>
				<tr>
					<td>One Sky Above Us</td>
					<td>07:34</td>
					<td><iframe class="play" src="https://bandcamp.com/EmbeddedPlayer/album=4236207006/size=small/bgcol=333333/linkcol=0f91ff/artwork=none/track=3898061310/transparent=true/"></iframe></td>
				</tr>
			</table>	
            
			<div class="commentSection">
				<div class="sendComment">
					<form action="/submit" method="post">
						<div class="usernameSection">
							<input id="usernameBox" name="username" placeholder="Author" type="text"/>
							<div><input name="anonymous" id="anonymousBox" type="checkbox" value="yes"> Write anonymously </div>
							<input id="passwordBox" name="password" type="password" placeholder="Password"/>
							<input value="Send Comment" type="submit" />
						</div>
						<input id="commentBox" name="commentText" type="text" placeholder="Enter your toughts here!"/>
					</form>

				</div>
				<div class="allComments">
					%s
				</div>
				<script>
						var anonymousBox = document.getElementById("anonymousBox");
						var usernameBox = document.getElementById("usernameBox");

						anonymousBox.addEventListener( 'change', function() {

							if (anonymousBox.checked == true){
								usernameBox.disabled = true;
							}else {
								usernameBox.disabled = false;
							}

						});
					</script>
			</div>

			
			<img class="pageEndLogo" src="img/bottomTrees.svg" alt="If These Trees Could Talk">
		</div>
		<div class="footer">
			<a class="sources" href="sources.html">Sources</a>
			<span class="footerText">All music rights are owned by <a href="https://twitter.com/treescouldtalk">If These Trees Could Talk</a></span>
		</div>
	</div>
</body>
</html>''' % comment_list

    return page


