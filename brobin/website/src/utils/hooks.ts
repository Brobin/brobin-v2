import {
  Dispatch,
  SetStateAction,
  useCallback,
  useEffect,
  useState,
} from "react";

interface IUseLoader {
  loaded: boolean;
  setLoaded: Dispatch<SetStateAction<boolean>>;
  loading: boolean;
  setLoading: Dispatch<SetStateAction<boolean>>;
}

export const useLoader = (loadFunction: Function): IUseLoader => {
  /**
   * useState implementation that takes an async function and tells
   * you when its running (loading) and complete (loaded). Defaults
   * to not loaded, so when it is used, it will automatically get
   * called to load.
   */
  const [loaded, setLoaded] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);

  const load = useCallback(async () => {
    setLoading(true);
    await loadFunction();
    setLoaded(true);
    setLoading(false);
  }, [loadFunction]);

  useEffect(() => {
    // Use dual booleans in case the loadFunction takes a long time.
    // We don't want to double call APIs and whatnot
    if (!loaded && !loading) {
      load();
    }
  }, [loaded, loading, load]);

  return { loaded, setLoaded, loading, setLoading };
};
