# No python is required for this task
# I found cryptohack domain names on web search tool: https://ui.ctsearch.entrust.com/ui/ctsearchui
# I received 14 records:
	# Issuer Name	Serial Number	Subject CN	Valid From	Valid To	Validation	Signing Algorithm	Key	SAN Count
# Let's Encrypt (14)									
	# Let's Encrypt	3f71c366a9fffdb001cb4fbf68e451cfc32	thetransparencyflagishere.cryptohack.org	04.09.2021	03.12.2021	non-EV	SHA-256	RSA-2048	1
	# Let's Encrypt	3f71c366a9fffdb001cb4fbf68e451cfc32	thetransparencyflagishere.cryptohack.org	04.09.2021	03.12.2021	non-EV	SHA-256	RSA-2048	1
	# Let's Encrypt	4d2695eee8a1a7214e0de7ad20ec151c08a	web.cryptohack.org	10.09.2021	09.12.2021	non-EV	SHA-256	RSA-2048	1
	# Let's Encrypt	4d2695eee8a1a7214e0de7ad20ec151c08a	web.cryptohack.org	10.09.2021	09.12.2021	non-EV	SHA-256	RSA-2048	1
	# Let's Encrypt	3d462e4c9259cbea35dd689fb45c3c897ea	cryptohack.org	18.09.2021	17.12.2021	non-EV	SHA-256	RSA-2048	3
	# Let's Encrypt	3d462e4c9259cbea35dd689fb45c3c897ea	cryptohack.org	18.09.2021	17.12.2021	non-EV	SHA-256	RSA-2048	3
	# Let's Encrypt	3a59fd0e37b7e6532fcddae2c1a3ce21ab8	blog.cryptohack.org	07.10.2021	05.01.2022	non-EV	SHA-256	RSA-2048	1
	# Let's Encrypt	3a59fd0e37b7e6532fcddae2c1a3ce21ab8	blog.cryptohack.org	07.10.2021	05.01.2022	non-EV	SHA-256	RSA-2048	1
	# Let's Encrypt	3cedd0cd4fbe346c6ee7389a43bd4ff4a8b	thetransparencyflagishere.cryptohack.org	03.11.2021	01.02.2022	non-EV	SHA-256	RSA-2048	1
	# Let's Encrypt	3cedd0cd4fbe346c6ee7389a43bd4ff4a8b	thetransparencyflagishere.cryptohack.org	03.11.2021	01.02.2022	non-EV	SHA-256	RSA-2048	1
	# Let's Encrypt	3f15d3070c26ab03c05a7d3d75e01d6c287	web.cryptohack.org	09.11.2021	07.02.2022	non-EV	SHA-256	RSA-2048	1
	# Let's Encrypt	3f15d3070c26ab03c05a7d3d75e01d6c287	web.cryptohack.org	09.11.2021	07.02.2022	non-EV	SHA-256	RSA-2048	1
	# Let's Encrypt	490617dedb5641ce459d49b566ff0517cf7	cryptohack.org	17.11.2021	15.02.2022	non-EV	SHA-256	RSA-2048	3
	# Let's Encrypt	490617dedb5641ce459d49b566ff0517cf7	cryptohack.org	17.11.2021	15.02.2022	non-EV	SHA-256	RSA-2048	3

# the first which I examined was: thetransparencyflagishere.cryptohack.org, and.... voila.. flag was there: 
# crypto{thx_redpwn_for_inspiration}