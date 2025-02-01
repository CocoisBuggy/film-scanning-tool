import edsdk

from src.core.session import EosSession

if __name__ == "__main__":
    with EosSession() as session:

        @session.on
        def camera_connected(camera):
            print(camera)

        session.connect()
