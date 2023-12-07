# If macOS eventually changes, then edit the first part of the if statement

import platform

print("Welcome to this simple program that tells you what operating system you're currently using!")
print("")

os = platform.system()

# The reason for this if-statement, is to make sure that it emphasizes that the "Darwin" output = the core Unix operating system of MacOS, iOS, etc. It may be confusing for newbies otherwise

if os == 'Darwin':
    print("Current OS: " + os +
          " (macOS, iOS, watchOS, tvOS, iPadOS, visionOS, and bridgeOS)")
else:
    print("Current OS: " + os)
